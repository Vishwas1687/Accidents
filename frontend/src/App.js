import { MapContainer, Marker, TileLayer, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { data } from "./data";
import L from "leaflet";
import icon from "leaflet/dist/images/marker-icon.png";
import "./App.css";
import { useEffect, useState } from "react";

const marker = L.icon({ iconUrl: icon });

const customMarker = L.icon({
  iconUrl: icon,
  iconSize: [25, 35],
  iconAnchor: [12, 35],
});

const center = [12.9254150390625, 74.871826171875];

const App = () => {
  const mapPolygonColorToDensity = (density) => {
    return density > 2
      ? "#a50f15"
      : density > 1
      ? "#de2d26"
      : density > 0.7
      ? "#fb6a4a"
      : density > 0.5
      ? "#fc9272"
      : density > 0.1
      ? "#fcbba1"
      : "#fee5d9";
  };
  const style = (feature) => {
    return {
      fillColor: mapPolygonColorToDensity(feature.properties.density),
      weight: 1,
      opacity: 1,
      color: "white",
      dashArray: "2",
      fillOpacity: 0.5,
    };
  };
  return (
    <MapContainer center={center} zoom={11}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {data.map((item, index) => {
        console.log(
          "GeoJSON data for item",
          index + 1,
          ":",
          item.geojson.features
        );
        return (
          <GeoJSON key={index} data={item.geojson.features} style={style} />
        );
      })}
    </MapContainer>
  );
};

export default App;
