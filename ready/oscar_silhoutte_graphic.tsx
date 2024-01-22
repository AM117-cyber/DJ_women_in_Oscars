import React, { useEffect, useState } from 'react';
import jsonData from './oscar_general.json';
import StatueComponent from "./statue-component";

const FilterByDateStatueComponent = ({ }) => {
    const [startYear, setStartYear] = useState(1973);
    const [endYear, setEndYear] = useState(2023);
    const [malePercentage, setMalePercentage] = useState(1);

    function CalculateMalePercentage(startYear: number, endYear: number) {
      var total = 0;
      let maleCount = 0;
      for (const year in jsonData) {
        if (+year >= startYear && +year <= endYear) {
          for (const category in jsonData[year]) {
            for (const nominee in jsonData[year][category]) {

              if (jsonData[year][category][nominee].gender === 'male') {
                maleCount++;
              }
              total++;
            }
          }
        }
      }
      var totalMalePercent = maleCount / total;
      return totalMalePercent;
    }

  function updateGraph(startYear: number, endYear: number): void {
    startYear = Math.min(Math.max(startYear, 1973), 2022);
    endYear = Math.max(Math.min(endYear, 2023), 1974);
    setStartYear(startYear);
    setEndYear(endYear);
    var totalMalePercent = CalculateMalePercentage(startYear, endYear);
    setMalePercentage(totalMalePercent);
  }

  useEffect( () => updateGraph(1973,2023), [])
    return (
        <div style={{display:"flex",width: "fit-content", flexDirection: "column", alignItems: "center", margin:"auto"}}>
                <div>
                  <label>
                    Año Inicial:
                    <input style={{marginLeft:5, width:50}} type="number" value={startYear} onChange={e => updateGraph(+e.target.value,endYear)} min={1973} max={endYear-1} />
                </label>
                <label>
                    Año Final:
                    <input onKeyDown={x => false} style={{marginLeft:5, width:50}} type="number" value={endYear} onChange={e => updateGraph(startYear,+e.target.value)} min={startYear+1} max={2023} />
                </label>
                </div>
            <StatueComponent percentage={malePercentage} height={300}/>
        </div>
    );
};

export default FilterByDateStatueComponent;