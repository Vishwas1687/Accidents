import React,{useState,useEffect} from 'react'
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import {addressPoints} from '../../utils/HeatmapUtils'
const Heatmap = ({map,mapRef}) => {
  const addressPoints = [
    [12.9254150390625, 74.871826171875, 1],
    [12.9254150390625, 74.8828125, 1],
    [12.930908203125, 74.8828125, 1],
  ];

  for (let i = 0; i < 3000; i++) {
    const latitude = getRandomNumberInRange(12.85, 13.10);
    const longitude = getRandomNumberInRange(74.8, 75.0);
    const value = 1;

    addressPoints.push([latitude, longitude, value]);
}

function getRandomNumberInRange(min, max) {
    return Math.random() * (max - min) + min;
}

  return (
    <>
    {map && (
      <HeatmapLayer
        fitBoundsOnLoad
        fitBoundsOnUpdate
        points={addressPoints}
        blur={40}
        longitudeExtractor={(m) => m[1]}
        latitudeExtractor={(m) => m[0]}
        intensityExtractor={(m) => parseFloat(m[2])}
        radius={25}
      />
    )}
    </>
  )
}

export default Heatmap