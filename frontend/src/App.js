import {
  MapContainer,
  Marker,
  TileLayer,
  GeoJSON,
  LayersControl,
  LayerGroup,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { data, data2, data3 } from "./data";
import { style, legendMapper, findColor2 } from "./utils";
import L from "leaflet";
import icon from "leaflet/dist/images/marker-icon.png";
import "./App.css";
import { useEffect, useState } from "react";

// const marker = L.icon({ iconUrl: icon });

// const customMarker = L.icon({
//   iconUrl: icon,
//   iconSize: [25, 35],
//   iconAnchor: [12, 35],
// });

const center = [12.9254150390625, 74.871826171875];

const App = () => {
  const category = "type_of_accident,weather_condition";
  // const mapPolygonColorToDensity = (density) => {
  //   return density > 2
  //     ? "#a50f15"
  //     : density > 1
  //     ? "#de2d26"
  //     : density > 0.7
  //     ? "#fb6a4a"
  //     : density > 0.5
  //     ? "#fc9272"
  //     : density > 0.1
  //     ? "#fcbba1"
  //     : "#fee5d9";
  // };
  // const style = (feature) => {
  //   return {
  //     fillColor: mapPolygonColorToDensity(feature.properties.density),
  //     weight: 1,
  //     opacity: 1,
  //     color: "white",
  //     dashArray: "2",
  //     fillOpacity: 0.5,
  //   };
  // };
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
  return (
    <>
      {Object.keys(onSelect).length != 0 ? (
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
      )}
      <MapContainer center={center} zoom={11}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {/* {data.map((item, index) => {
        console.log(
          "GeoJSON data for item",
          index + 1,
          ":",
          item.geojson.features
        );
        return (
          <GeoJSON key={index} data={item.geojson.features} style={style} />
        );
      })} */}

        {data3.map((item, index) => (
          <GeoJSON
            key={index}
            data={item.geojson.features}
            style={style}
            onEachFeature={onEachFeature}
          />
        ))}
      </MapContainer>
    </>
  );

  // return (
  //   <MapContainer center={[40.44695, -345.23437]} zoom={2}>
  //     <LayersControl>
  //       <LayersControl.BaseLayer name="Open Street Map">
  //         <TileLayer
  //           attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  //           url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
  //         />
  //       </LayersControl.BaseLayer>

  //       <LayersControl.BaseLayer checked name="Google Map">
  //         <TileLayer
  //           attribution="Google Maps"
  //           url="https://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}"
  //         />
  //       </LayersControl.BaseLayer>

  //       <LayersControl.BaseLayer name="Google Map Satellite">
  //         <LayerGroup>
  //           <TileLayer
  //             attribution="Google Maps Satellite"
  //             url="https://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}"
  //           />
  //           <TileLayer url="https://www.google.cn/maps/vt?lyrs=y@189&gl=cn&x={x}&y={y}&z={z}" />
  //         </LayerGroup>
  //       </LayersControl.BaseLayer>
  //     </LayersControl>
  //   </MapContainer>
  // );
};

export default App;
