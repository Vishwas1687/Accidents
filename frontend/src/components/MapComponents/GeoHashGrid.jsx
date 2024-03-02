import React from 'react'
import { GeoJSON } from 'react-leaflet';
import { data} from "../../data";
import { style } from"../../utils/GridUtils"
const GeoHashGrid = () => {
  // const category = "type_of_accident,weather_condition";
  // const [onSelect, setOnSelect] = useState([]);

  // const highlightFeature = (e) => {
  //   const layer = e.target;
  //   const category_split = e.target.feature.properties[`${category}`];
  //   setOnSelect(category_split);
  //   layer.setStyle({
  //     weight: 1,
  //     color: "black",
  //     fillOpacity: 1,
  //   });
  // };

  // const resetHighlight = (e) => {
  //   setOnSelect([]);
  //   e.target.setStyle(style(e.target.feature));
  // };

  // const onEachFeature = (feature, layer) => {
  //   layer.on({
  //     mouseover: highlightFeature,
  //     mouseout: resetHighlight,
  //   });
  // };
  return (
    <div>
      {data.map((item, index) => (
          <GeoJSON
            key={index}
            data={item.geojson.features}
            style={style}
            // onEachFeature={onEachFeature}
          />
        ))}
    </div>
  )
}

export default GeoHashGrid