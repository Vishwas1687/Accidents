// const category = "type_of_accident,weather_condition";

const colorMapper = {
    High: "",
    Medium: "",
    Low: "",
    "Very low": "",
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
  
  export const findColor2 = (density) => {
    setUpColors();
  
    if (density > 40) {
      return colorMapper["High"]; // Assign a color for density > 40
    } else if (density > 20) {
      return colorMapper["Medium"]; // Assign a color for density > 20
    } else if (density > 5) {
      return colorMapper["Low"]; // Assign a color for density > 5
    } else {
      return colorMapper["Very Low"]; // Assign a color for density<5
    }
  };
  
  export const style = (feature) => {
    return {
      fillColor: findColor2(feature.properties.density),
      weight: 1,
      opacity: 1,
      color: "white",
      dashArray: "2",
      fillOpacity: 0.5,
    };
  };
  
  // const setUpColors = () => {
  //   let i = 0;
  //   for (let key in colorMapper) {
  //     colorMapper[key] = colors[i];
  //     i = i + 1;
  //   }
  // };
  
  // export const findColor2 = (category_split) => {
  //   setUpColors();
  //   const type = category_split[0].type;
  //   return colorMapper[type];
  // };
  
  // const findColor = (category_split) => {
  //   const length = category_split.length;
  //   const color_split = colors.slice(0, length);
  //   let max_accidents = 0;
  //   let index = -1;
  //   for (let i = 0; i < length; i++) {
  //     if (category_split[i].accidents > max_accidents) {
  //       max_accidents = category_split[i].accidents;
  //       index = i;
  //     }
  //   }
  //   return colors[index];
  // };
  // export const style = (feature) => {
  //   return {
  //     fillColor: findColor2(feature.properties[`${category}`]),
  //     weight: 1,
  //     opacity: 1,
  //     color: "white",
  //     dashArray: "2",
  //     fillOpacity: 0.5,
  //   };
  // };
  