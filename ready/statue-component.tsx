import React from 'react';

const StatueComponent = ({percentage, height=500}:{percentage:number, height?:number}) => {
    const aspectRatio = 0.377;
    return (
        <div style={{width: height*aspectRatio, height:height, backgroundColor: "pink", textAlign:"center"}}>
           <div style={{height:height*percentage, backgroundColor: "blue"}}>
              <img style={{height:height, margin:"auto"}} src="..\image\charts\award.png"/>
            </div>
            <div style={{margin:"auto"}}><span>{100 - Math.round(percentage*100)}</span> %</div>
        </div>
    );
};

export default StatueComponent;