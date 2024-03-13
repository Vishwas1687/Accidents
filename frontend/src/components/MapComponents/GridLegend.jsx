import React,{useEffect} from 'react'
import '../../utils/GridLegend.css'
const GridLegend = ({colorMapper,breakpoints,isGridChecked}) => {
    return (
        <>
        <div className='info legend' style={{'zIndex':`${isGridChecked?1000:0}`}}>
    {Object.keys(colorMapper).map((record) => (
        <div key={record} style={{
            height: '2rem',
            }}>
            <span style={{
                backgroundColor: colorMapper[record],
                height: '0.8rem',
                width: '0.8rem',
                border: '2px solid black',  // Specify border style and color
                display: 'inline-block',   // Ensure inline-block display for proper alignment
                marginRight: '0.5rem'       // Add margin for separation
            }}></span>
            <span style={{ 'font-size':'1.2rem'}}>Above {breakpoints[record].toFixed(2)}</span>
        </div>
    ))}
</div>

</>
    )
}

export default GridLegend