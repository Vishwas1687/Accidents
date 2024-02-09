import React, { useEffect, useRef, useState } from "react";
import {
  MapContainer,
  Marker,
  TileLayer,
  GeoJSON,
  LayersControl,
  LayerGroup,
} from "react-leaflet";
import MarkerClusterGroup from "react-leaflet-cluster";
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import { style, legendMapper, findColor2 } from "./utils";
import icon from "leaflet/dist/images/marker-icon.png";
import { data, data2, data3 } from "./data";
import "./App.css";

const center = [12.9254150390625, 74.871826171875];

const customMarker = L.icon({
  iconUrl: icon,
  iconSize: [25, 35],
  iconAnchor: [12, 35],
});

const App = () => {
  const mapRef = useRef(null);
  const addressPoints = [
    [12.9254150390625, 74.871826171875, 1],
    [12.9254150390625, 74.8828125, 2],
    [12.930908203125, 74.8828125, 3],
    [12.930908203125, 74.86083984375, 2],
    [12.9583740234375, 74.871826171875, 3],
    [12.9583740234375, 74.8828125, 10],
    [12.9638671875, 74.8828125, 5],
    [12.9638671875, 74.871826171875, 1],
  ];

  const category = "type_of_accident,weather_condition";
  const [onSelect, setOnSelect] = useState([]);
  const [isHeatmapChecked, setIsHeatmapChecked] = useState(false);
  const [isGridChecked, setIsGridChecked] = useState(true);
  const [map, setMap] = useState();

  const highlightFeature = (e) => {
    const layer = e.target;
    const category_split = e.target.feature.properties[`${category}`];
    setOnSelect(category_split);
    layer.setStyle({
      weight: 1,
      color: "black",
      fillOpacity: 1,
    });
  };

  const resetHighlight = (e) => {
    setOnSelect([]);
    e.target.setStyle(style(e.target.feature));
  };

  const onEachFeature = (feature, layer) => {
    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
    });
  };

  useEffect(() => {
    setMap(mapRef.current);
  }, [map]);

  return (
    <>
      {isGridChecked && onSelect.length !== 0 && (
        <div className="location-detail">
          <ul className="category-accidents">
            {onSelect.map((cat) => (
              <li key={cat.type}>
                {cat.type} - {cat.accidents}
              </li>
            ))}
          </ul>
        </div>
      )}

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
            {map && (
              <HeatmapLayer
                fitBoundsOnLoad
                fitBoundsOnUpdate
                points={addressPoints}
                longitudeExtractor={(m) => m[1]}
                latitudeExtractor={(m) => m[0]}
                intensityExtractor={(m) => parseFloat(m[2])}
                radius={25}
              />
            )}
          </LayersControl.Overlay>
          <LayersControl.Overlay
            checked={isGridChecked}
            name="Grid"
            onChange={() => setIsGridChecked((prev) => !prev)}
          >
            <LayerGroup>
              {data3.map((item, index) => (
                <GeoJSON
                  key={index}
                  data={item.geojson.features}
                  style={style}
                  onEachFeature={onEachFeature}
                />
              ))}
            </LayerGroup>
          </LayersControl.Overlay>
          <LayersControl.Overlay name="clusters">
            <MarkerClusterGroup chunkedLoading>
              {addressPoints.map((point, index) => (
                <Marker
                  key={index}
                  icon={customMarker}
                  position={[point[0], point[1]]}
                />
              ))}
            </MarkerClusterGroup>
          </LayersControl.Overlay>
        </LayersControl>
      </MapContainer>
    </>
  );
};

export default App;
