import {
    MapContainer,
    TileLayer,
    LayersControl,
    LayerGroup,
  } from "react-leaflet";
import MarkerClusterGroup from "react-leaflet-cluster";
import React,{useState,useEffect,useRef} from 'react'
import L from "leaflet";
import icon from "leaflet/dist/images/marker-icon.png";
import "../App.css";
import "leaflet/dist/leaflet.css";
import { createClusterCustomIcon } from "../utils/ClusterUtils";
import Heatmap from "./MapComponents/Heatmap";
import Cluster from './MapComponents/Cluster'
import GeoHashGrid from "./MapComponents/GeoHashGrid";

const Map = () => {
  const center = [12.9254150390625, 74.871826171875];
  const customMarker = L.icon({
    iconUrl: icon,
    iconSize: [25, 35],
    iconAnchor: [12, 35],
  });
    const mapRef = useRef(null);
  const [isHeatmapChecked, setIsHeatmapChecked] = useState(false);
  const [isGridChecked, setIsGridChecked] = useState(true);
  const [map, setMap] = useState();
  useEffect(() => {
    setMap(mapRef.current);
  }, [map]);

  return (
    <MapContainer center={center} zoom={12} ref={mapRef}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <LayersControl>
          <LayersControl.Overlay
            checked={isHeatmapChecked}
            name="Heatmap"
            onChange={() => setIsHeatmapChecked((prev) => !prev)}
          >
              <Heatmap map={map}/>
          </LayersControl.Overlay>
          <LayersControl.Overlay
            checked={isGridChecked}
            name="Grid"
            onChange={() => setIsGridChecked((prev) => !prev)}
          >
            <LayerGroup>
              <GeoHashGrid/>
            </LayerGroup>
          </LayersControl.Overlay>
          <LayersControl.Overlay name="clusters">
            <MarkerClusterGroup chunkedLoading
             iconCreateFunction={createClusterCustomIcon}
            >
              <Cluster customMarker={customMarker}/>
            </MarkerClusterGroup>
          </LayersControl.Overlay>
        </LayersControl>
      </MapContainer>
  )
}
export default Map
