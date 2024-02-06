const category = "type_of_accident,weather_condition";
const colorMapper = {
  "grievous and rainy": "",
  "minor and rainy": "",
  "no injury and rainy": "",
  "no injury and sunny": "",
  "fatal and sunny": "",
  "minor and sunny": "",
  "grievous and sunny": "",
  "fatal and rainy": "",
};
const colors = [
  "red",
  "green",
  "blue",
  "yellow",
  "orange",
  "pink",
  "grey",
  "black",
  "white",
];

const setUpColors = () => {
  let i = 0;
  for (let key in colorMapper) {
    colorMapper[key] = colors[i];
    i = i + 1;
  }
};

export const findColor2 = (category_split) => {
  setUpColors();
  const type = category_split[0].type;
  return colorMapper[type];
};

const findColor = (category_split) => {
  const length = category_split.length;
  const color_split = colors.slice(0, length);
  let max_accidents = 0;
  let index = -1;
  for (let i = 0; i < length; i++) {
    if (category_split[i].accidents > max_accidents) {
      max_accidents = category_split[i].accidents;
      index = i;
    }
  }
  return colors[index];
};
export const style = (feature) => {
  return {
    fillColor: findColor2(feature.properties[`${category}`]),
    weight: 1,
    opacity: 1,
    color: "white",
    dashArray: "2",
    fillOpacity: 0.5,
  };
};
