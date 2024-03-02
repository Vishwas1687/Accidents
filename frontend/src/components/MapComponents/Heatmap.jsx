import React from 'react'
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
const Heatmap = ({map}) => {
  const addressPoints = [
    [12.9254150390625, 74.871826171875, 1],
    [12.9254150390625, 74.8828125, 2],
    [12.930908203125, 74.8828125, 3],
    [12.930908203125, 74.86083984375, 2],
    [12.9583740234375, 74.871826171875, 3],
    [12.9583740234375, 74.8828125, 10],
    [12.9638671875, 74.8828125, 5],
    [12.9638671875, 74.871826171875, 1],
  ];
  return (
    <>
    {map && (
      <HeatmapLayer
        fitBoundsOnLoad
        fitBoundsOnUpdate
        points={addressPoints}
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