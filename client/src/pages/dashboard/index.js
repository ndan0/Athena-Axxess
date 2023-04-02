import {useEffect, useRef} from "react"

import Chart from 'chart.js/auto';

const sampleData = {
    dates: ["2023-03-26", "2023-03-27", "2023-03-28", "2023-03-29", "2023-03-30", "2023-03-31", "2023-04-01",
        "2023-04-02", "2023-04-03", "2023-04-04", "2023-04-05", "2023-04-06", "2023-04-07", "2023-04-08"],
    joy: [100, 93, 12, 32 , 12, 32, 12, 32, 12, 32, 12, 32, 12, 32],
    sad: [100, 93, 12, 32 , 21, 32, 12, 32, 0, 32, 12, 32, 12, 32],
    anger: [100, 93, 12, 32 , 12, 32, 12, 34, 12, 32, 12, 32, 12, 32],
    fear: [100, 93, 12, 32 , 90, 32, 12, 32, 12, 32, 90, 32, 12, 32],
    neutral: [100, 93, 12, 32 , 12, 32, 12, 32, 90, 32, 12, 32, 12, 32],
    risk: [100, 93, 12, 32 , 84, 32, 12, 32, 12, 32, 12, 0, 12, 32],

}

const displayData = keepLastNItems(sampleData, 7)
const xTitle = "Date"

function Example() {
  useEffect(() => {

      const emotionCanvas = document.getElementById('emotionChart');

      // Check if a chart is already created on the canvas
      if (emotionCanvas.chart) {
          // If a chart is already created, destroy it
          emotionCanvas.chart.destroy();
      }

      // Create a chart on the canvas for the first time
      const ctx1 = emotionCanvas.getContext('2d');

      var emotionChart = new Chart(ctx1, {
          type: 'line',
          data: {
              labels: displayData.dates,
              datasets: [{
                  data: displayData.joy,
                  label: "Joy",
                  borderColor: "rgb(255, 216, 125)",
                  backgroundColor: "rgb(255, 216, 125,0.1)",
              }, {
                  data: displayData.sad,
                  label: "Sad",
                  borderColor: "rgb(48, 103, 178)",
                  backgroundColor: "rgb(48, 103, 178,0.1)",
              }, {
                  data: displayData.anger,
                  label: "Anger",
                  borderColor: "rgb(196,88,80)",
                  backgroundColor: "rgb(196,88,80,0.1)",
              }, {
                  data: displayData.fear,
                  label: "Fear",
                  borderColor: "rgb(142, 82, 158)",
                  backgroundColor: "rgb(142, 82, 158,0.1)",
              }, {
                  data: displayData.neutral,
                  label: "Neutral",
                  borderColor: "rgb(146, 200, 94)",
                  backgroundColor: "rgb(146, 200, 94,0.1)",
              }
              ]
          },
          options: {
              plugins: {
                  title: {
                      display: true,
                      text: 'Chart Title',
                  }
              },
              scales: {
                  x: {
                      display: true,
                      title: {
                          display: true,
                          text: xTitle
                      }
                  },
                  y: {
                      display: true,
                      title: {
                          display: true,
                          text: 'Value'
                      },
                      min: 0,
                      max: 100,
                  }
              }
          }

      });
      // Store the chart instance on the canvas element
      emotionCanvas.chart = emotionChart;

      const riskCanvas = document.getElementById('riskChart');

      // Check if a chart is already created on the canvas
      if (riskCanvas.chart) {
          // If a chart is already created, destroy it
          riskCanvas.chart.destroy();
      }

      // Create a new chart on the canvas
      const ctx2 = riskCanvas.getContext('2d');

      var riskChart = new Chart(ctx2, {
          type: 'line',
          data: {
              labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
              datasets: [{
                  data: [86, 40, 90, 38, 10, 98, 100],
                  label: "Applied",
                  borderColor: "rgb(62,149,205)",
                  backgroundColor: "rgb(62,149,205,0.1)",
              }
              ]
          },
          options: {
              plugins: {
                  title: {
                      display: true,
                      text: 'Patient Risk Factor',
                  }
              },
              scales: {
                  x: {
                      display: true,
                      title: {
                          display: true,
                          text: 'Percentage'
                      }
                  },
                  y: {
                      display: true,
                      title: {
                          display: true,
                          text: 'Value'
                      },
                      min: 0,
                      max: 100,
                  }
              }
          }

      });
      // Store the chart instance on the canvas element
      riskCanvas.chart = riskChart;


  }, [])


  return (
      <>

        <div className="flex mx-auto my-auto h-full">
            <div className="flex flex-col border border-gray-400 pt-0 w-1/6 shadow-lg">
                <a className="w-full text-center ">Users</a>
                <a className="w-full text-center border border-gray-400">Dan</a>
                <a className="w-full text-center border border-gray-400">Abhishek</a>
                <a className="w-full text-center border border-gray-400">Jason</a>
                <a className="w-full text-center border border-gray-400">Cuma</a>

            </div>

            <div className="flex flex-col gap-2 w-2/5 px-12 pt-2">

            </div>

            <div className="flex flex-col gap-2 inset-y-0 right-0 w-2/5 px-12 pt-2">
              <div className='border border-gray-400 pt-0 rounded-xl w-full  shadow-lg'>

                <canvas id='emotionChart'></canvas>
              </div>
              <div className='border border-gray-400 pt-0 rounded-xl w-full shadow-lg'>
                <canvas id='riskChart'></canvas>
              </div>
            </div>
        </div>
      </>
  )
}


function keepLastNItems(dict, n) {
    if (n > dict.dates.length) {
        return dict;
    }
    const newDict = {};
    for (const key in dict) {
        const newKey = dict[key].slice(-n);
        newDict[key] = newKey;

    }
    return newDict;
}

export default Example;