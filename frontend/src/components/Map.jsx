import {
    MapContainer,
    TileLayer,
    LayersControl,
    LayerGroup,
  } from "react-leaflet";
import MarkerClusterGroup from "react-leaflet-cluster";
import React,{useState,useEffect,useRef} from 'react'
import {data,data4} from '../data.js'
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
  const [densityValues,setDensityValues]=useState({
    "0-25":0,
    "25-50":0,
    "50-75":0,
    "75-100":0
  })
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

  const getDensityValues=()=>{
    const values = data
    .map((record) => record.geojson.features[0].properties.density)
    .sort((a,b)=>a-b);

    const totalLength = values.length;

  const firstPercentile = values.slice(0, Math.ceil(totalLength * 0.25));
  const secondPercentile = values.slice(
    Math.ceil(totalLength * 0.25),
    Math.ceil(totalLength * 0.5)
  );
  const thirdPercentile = values.slice(
    Math.ceil(totalLength * 0.5),
    Math.ceil(totalLength * 0.75)
  );
  const fourthPercentile = values.slice(Math.ceil(totalLength * 0.75));
  const value_obj={
    "0-25":firstPercentile[0],
    "25-50":secondPercentile[0],
    "50-75":thirdPercentile[0],
    "75-100":fourthPercentile[0]
  }
  console.log(firstPercentile,secondPercentile,thirdPercentile,fourthPercentile)
    setDensityValues(value_obj)
  }

  useEffect(()=>{
    if(isGridChecked)
    getDensityValues()
  },[isGridChecked])



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
            onAdd={() => setIsHeatmapChecked(true)}
             onRemove={() => setIsHeatmapChecked(false)}
          >
              <Heatmap map={map} mapRef={mapRef}/>
          </LayersControl.Overlay>
          <LayersControl.Overlay
            checked={isGridChecked}
            name="Grid"
            onAdd={() => setIsGridChecked(true)}
            onRemove={() => setIsGridChecked(false)}
          >
            <LayerGroup>
              {console.log(isGridChecked)}
              <GeoHashGrid map={map} breakpoints={densityValues} isGridChecked={isGridChecked}/>
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
