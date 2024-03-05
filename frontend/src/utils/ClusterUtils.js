import L from 'leaflet';
import './Cluster.css'
export const createClusterCustomIcon=(cluster)=>{
    const count = cluster.getChildCount();
  let size = 'Large2XL';

  if (count < 10) {
    size = 'Small';
  }
  else if (count >= 10 && count < 100) {
    size = 'Medium';
  }
  else if (count >= 100 && count < 300) {
    size = 'Large';
  }
  else if (count >= 300 && count < 500) {
    size = 'LargeXL';
  }
  const options = {
    cluster: `markerCluster${size}`,
  };

  function calculateCustomDimension(count) {
    const calculateHeightWidth = (countMultiplier) => `${Math.log(count * countMultiplier)}rem`;
    const calculateFontSize = (countMultiplier) => `${Math.log(count * countMultiplier)}rem`;

    let height, width, fontSize;

    if (count < 5) {
        height = calculateHeightWidth(10);
        width = calculateHeightWidth(10);
        fontSize = calculateFontSize(1);
    } else if (count < 10) {
        height = calculateHeightWidth(8);
        width = calculateHeightWidth(8);
        fontSize = calculateFontSize(0.5);
    } else if (count < 50) {
        height = calculateHeightWidth(5);
        width = calculateHeightWidth(5);
        fontSize = calculateFontSize(0.2);
    } else if(count<150) {
        height = calculateHeightWidth(2);
        width = calculateHeightWidth(2);
        fontSize = calculateFontSize(0.05);
    }
    else if(count<300) {
      height = calculateHeightWidth(1);
      width = calculateHeightWidth(1);
      fontSize = calculateFontSize(0.02);
  }
   else if(count<500) {
    height = calculateHeightWidth(0.5);
    width = calculateHeightWidth(0.5);
    fontSize = calculateFontSize(0.01);
  }
  else if(count<1000) {
    height = calculateHeightWidth(0.3);
    width = calculateHeightWidth(0.3);
    fontSize = calculateFontSize(0.007);
  }
  else{
    height = calculateHeightWidth(0.2);
    width = calculateHeightWidth(0.2);
    fontSize = calculateFontSize(0.003);
  }

    return {
        "height": height,
        "width": width,
        "fontSize": fontSize,
    };
}
const customDimension = calculateCustomDimension(count);
  return L.divIcon({
        html:
          `<div class=${options.cluster} 
          style="height:${customDimension.height};
          width:${customDimension.width};
          font-size:${customDimension.fontSize}">
            <span class="markerClusterLabel">${count}</span>
          </div>`,
      })
    }