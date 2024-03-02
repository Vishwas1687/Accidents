import React from 'react'
import { Marker } from 'react-leaflet';
const Cluster = ({customMarker}) => {
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
    <div> 
      {addressPoints.map((point, index) => (
      <Marker
        key={index}
        icon={customMarker}
        position={[point[0], point[1]]}
      />
    ))}
    </div>
  )
}

export default Cluster