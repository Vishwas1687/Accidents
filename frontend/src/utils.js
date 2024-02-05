const category = "type_of_accident";
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
    fillColor: findColor(feature.properties[`${category}`]),
    weight: 1,
    opacity: 1,
    color: "white",
    dashArray: "2",
    fillOpacity: 0.5,
  };
};
