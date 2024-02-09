import React, { useEffect, useRef, useState } from "react";
import {
  MapContainer,
  Marker,
  TileLayer,
  GeoJSON,
  LayersControl,
  LayerGroup,
} from "react-leaflet";
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import "leaflet/dist/leaflet.css";
import { style, legendMapper, findColor2 } from "./utils";
import icon from "leaflet/dist/images/marker-icon.png";
import { data, data2, data3 } from "./data";
import "./App.css";

const center = [12.9254150390625, 74.871826171875];

const App = () => {
  const mapRef = useRef(null);
  const addressPoints = [
    [12.9254150390625, 74.871826171875, 1],
    [12.9254150390625, 74.8828125, 2],
    [12.930908203125, 74.8828125, 3],
    [12.930908203125, 74.86083984375, 2],
  ];

  const category = "type_of_accident,weather_condition";
  const [onSelect, setOnSelect] = useState([]);

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
  const map = mapRef.current;

  return (
    <>
      {/* {Object.keys(onSelect).length != 0 ? (
        <div className="location-detail">
          <ul className="category-accidents">
            {onSelect.map((cat) => (
              <li key={cat.type}>
                {cat.type} - {cat.accidents}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div className="location-detail">hello</div>
      )} */}
      <MapContainer center={center} zoom={12} ref={mapRef}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
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
        {/* {data3.map((item, index) => (
          <GeoJSON
            key={index}
            data={item.geojson.features}
            style={style}
            onEachFeature={onEachFeature}
          />
        ))} */}
      </MapContainer>
    </>
  );
};

export default App;
