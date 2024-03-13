// const category = "type_of_accident,weather_condition";
export const colorMapper = {
  "75-100":"",
  "50-75":"",
  "25-50":"",
  "0-25":"",
    
    
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
  
  export const setUpColors = () => {
    let i = 0;
    for (let key in colorMapper) {
      colorMapper[key] = colors[i];
      i = i + 1;
    }
  };
  
  export const findColor2 = (density,breakpoints) => {
    setUpColors();
    if(Object.keys(breakpoints).length!==0)
    {
      if (density >=breakpoints["75-100"]) {
        return colorMapper["75-100"]; // Assign a color for density > 40
      } else if (density >=breakpoints["50-75"]) {
        return colorMapper["50-75"]; // Assign a color for density > 20
      } else if (density >= breakpoints["25-50"]) {
        return colorMapper["25-50"]; // Assign a color for density > 5
      } else {
        return colorMapper["0-25"]; // Assign a color for density<5
      }
    }
    
  };
  
  export const style = (feature,breakpoints) => {
    return {
      fillColor: findColor2(feature?.properties?.density,breakpoints),
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
  