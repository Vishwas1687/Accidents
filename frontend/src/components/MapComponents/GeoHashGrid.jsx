import React from 'react'
import { GeoJSON } from 'react-leaflet';
import { data} from "../../data";
import { style,colorMapper,setUpColors} from"../../utils/GridUtils"
import GridLegend from './GridLegend';
const GeoHashGrid = ({map,breakpoints}) => {
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
            style={(feature)=>style(feature,breakpoints)}
            // onEachFeature={onEachFeature}
          />
        ))}
        {map && <GridLegend map={map} colorMapper={colorMapper} breakpoints={breakpoints}/>}
    </div>
  )
}

export default GeoHashGrid