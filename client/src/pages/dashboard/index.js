import {useEffect, useRef, useState} from "react"

import Chart from 'chart.js/auto';
import {patchConsoleError} from "next/dist/client/components/react-dev-overlay/internal/helpers/hydration-error-info";
import {data} from "autoprefixer";


const xTitle = "Date"


function Example() {

    const [emotionData, setEmotionData] = useState({dates: [], joy: [], sad: [], anger: [], fear: [], neutral: []})
    const [user, SetUser] = useState("user1")
    const [dateEmotion, setDateEmotion] = useState(getDateFromToday(7))
    const [daysEmotion, setDaysEmotion] = useState(7)
    const [dateHeart, setDateHeart] = useState(getDateFromToday(7))
    const [daysHeart, setDaysHeart] = useState(7)
    const [dateCalorie, setDateCalorie] = useState(getDateFromToday(7))
    const [daysCalorie, setDaysCalorie] = useState(7)
    const date = "2023-01-01"
    const days = 7

    const [randomListofWord, setStateChange] = useState(['happy', 'sad', 'angry', 'fear', 'neutral', 'jo', 'game'])


    useEffect(() => {
        const action = async () => {
            const res = await fetch("https://6a44-129-110-241-55.ngrok.io/dashboard/keywords/2023-01-01/7")
            const data = await res.json()
            setStateChange(data[data.length-1].keywords.split("|"))
        }
        action()
    }, [])
    useEffect(() => {
        // days = 7;

        const emotionAction = async () => {

            const res = await fetch("https://6a44-129-110-241-55.ngrok.io/dashboard/emotion/" + date + "/" + days)
            const rawData = await res.json()

            // const rawData = []
            //
            let dateArr = []
            let joyArr = []
            let sadArr = []
            let angerArr = []
            let fearArr = []
            console.log("hey", rawData)

            for (let i = 0; i < rawData.length; i++) {
                dateArr.push(rawData[i].date)
                joyArr.push(rawData[i].emotions[0].score*100)
                sadArr.push(rawData[i].emotions[1].score*100)
                angerArr.push(rawData[i].emotions[2].score*100)
                fearArr.push(rawData[i].emotions[3].score*100)
            }

            console.log({joyArr})

            emotionData["dates"] = dateArr
            emotionData["joy"] = joyArr
            emotionData["sad"] = sadArr
            emotionData["anger"] = angerArr
            emotionData["fear"] = fearArr

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
                    labels: emotionData.dates,
                    datasets: [{
                        data: emotionData.joy,
                        label: "Joy",
                        borderColor: "rgb(255, 216, 125)",
                        backgroundColor: "rgb(255, 216, 125,0.1)",
                    }, {
                        data: emotionData.sad,
                        label: "Sad",
                        borderColor: "rgb(48, 103, 178)",
                        backgroundColor: "rgb(48, 103, 178,0.1)",
                    }, {
                        data: emotionData.anger,
                        label: "Anger",
                        borderColor: "rgb(196,88,80)",
                        backgroundColor: "rgb(196,88,80,0.1)",
                    }, {
                        data: emotionData.fear,
                        label: "Fear",
                        borderColor: "rgb(142, 82, 158)",
                        backgroundColor: "rgb(142, 82, 158,0.1)",
                    }
                        //, {
                        //     data: emotionData.neutral,
                        //     label: "Neutral",
                        //     borderColor: "rgb(146, 200, 94)",
                        //     backgroundColor: "rgb(146, 200, 94,0.1)",
                        // }
                    ]
                },
                options: {
                    plugins: {
                        title: {
                            display: false,
                            text: "Emotional Health",
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
                                text: 'Percentage'
                            },
                            min: 0,
                            max: 100,
                        }
                    }
                }

            });
            // Store the chart instance on the canvas element
            emotionCanvas.chart = emotionChart;


        }

        emotionAction()

    }, [dateEmotion])
    useEffect(() => {
        const heartAction = async () => {

            const rawData = [
                {
                    date: "2021-01-01",
                    avg_hrt: 70
                },
                {
                    date: "2021-01-02",
                    avg_hrt: 70
                },
                {
                    date: "2021-01-03",
                    avg_hrt: 70
                },{
                    date: "2021-01-04",
                    avg_hrt: 70
                },

            ]

            // const res = await fetch("https://6a44-129-110-241-55.ngrok.io/dashboard/heart/" + date+ "/" + days)
            // const rawData = await res.json()

            let dateArr = []
            let heartArr = []
            console.log({rawData})
            for (let i = 0; i < rawData.length; i++) {
                dateArr.push(rawData[i].date)
                heartArr.push(rawData[i].avg_hrt)
            }

            const heartCanvas = document.getElementById('heartChart');

            // Check if a chart is already created on the canvas
            if (heartCanvas.chart != null) {
                // If a chart is already created, destroy it
                try {
                    heartCanvas.chart.destroy();
                } catch (e) {
                    console.log(e)
                }

            }

            // Create a new chart on the canvas
            const ctx2 = heartCanvas.getContext('2d');

            console.log({heartArr})

            var heartChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: dateArr,
                    datasets: [{
                        data: heartArr,
                        label: "Heart Rate",
                        borderColor: "rgb(185, 36, 60)",
                        backgroundColor: "rgb(185, 36, 60,0.1)",
                    }
                    ]
                },
                options: {
                    plugins: {
                        title: {
                            display: false,
                            text: 'Heart Rate',
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

                        }
                    }
                }

            });
            // Store the chart instance on the canvas element
            heartCanvas.chart = heartChart;
        }
        heartAction()
    }, [dateHeart])

    useEffect(() => {
        const calorieAction = async () => {

            // const rawData = []

            const res = await fetch("https://6a44-129-110-241-55.ngrok.io/dashboard/calories/" + date+ "/" + days)
            const rawData = await res.json()

            let dateArr = []
            let heartArr = []

            for (let i = 0; i < rawData.length; i++) {
                dateArr.push(rawData[i].date)
                heartArr.push(rawData[i].calories)
            }

            const heartCanvas = document.getElementById('calorieChart');

            // Check if a chart is already created on the canvas
            if (heartCanvas.chart != null) {
                // If a chart is already created, destroy it
                try {
                    heartCanvas.chart.destroy();
                } catch (e) {
                    console.log(e)
                }

            }

            // Create a new chart on the canvas
            const ctx2 = heartCanvas.getContext('2d');

            var heartChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: dateArr,
                    datasets: [{
                        data: heartArr,
                        label: "Calorie Burnt",
                        borderColor: "rgb(255, 216, 125)",
                        backgroundColor: "rgb(255, 216, 125,0.1)",
                    }
                    ]
                },
                options: {
                    plugins: {
                        title: {
                            display: false,
                            text: 'Calorie Burnt',
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

                        }
                    }
                }

            });
            // Store the chart instance on the canvas element
            heartCanvas.chart = heartChart;
        }

        calorieAction()

    }, [dateCalorie])
  return (
      <>

        <div className="flex mx-auto my-auto h-full">
            <div className="flex flex-col border border-gray-400 p-0 w-1/6 shadow-lg">
                <a className="w-full text-center border border-gray-400 py-2 text-white bg-axx-red">Patient</a>
                <a className="w-full text-center ">Name: Abhishek Mishra</a>
                <a className="w-full text-center ">Age: 21</a>
                <a className="w-full text-center">Gender: Male</a>
                <a className="w-full text-center">Weight: 180lb</a>
                <a className="w-full text-center">Height: 5 ft 10 in</a>
                <a className="w-full text-center">Contact: 972-000-0000</a>
                <a className="w-full text-center">Last Hospitalized: 2023-01-01</a>
                <a className="w-full text-center">HIPPA Status: Non-Restricted</a>



            </div>

            <div className="flex flex-col gap-2 w-2/5 px-12 pt-2">
                <div className='flex flex-col border border-gray-400 pt-0 rounded-xl w-full shadow-lg'>
                    <a className="text-center justify-center font-bold">Calorie</a>
                    <canvas id='calorieChart'></canvas>
                    <select className="ml-2 rounded-md w-32" id="Calorie" onChange={(e) =>
                    {var selectBox = document.getElementById("Calorie");
                        const dayAway = selectBox.options[selectBox.selectedIndex].value;
                        setDateCalorie(getDateFromToday(dayAway))
                        setDaysCalorie(parseInt(dayAway));
                    }}>
                        <option value="7">Last 7 days</option>
                        <option value="30">Last 30 days</option>
                        <option value="365">Last 365 days</option>
                    </select>
                </div>
                <div className='flex flex-col border border-gray-400 pt-0 mt-7 h-2/5 rounded-xl w-full shadow-lg'>
                    <a className="text-center justify-center font-bold">Most common word/topic counts</a>
                    <div className="mx-2 flex flex-row h-5/6 grid grid-cols-2">
                        {randomListofWord.map((word, index) => <p key={index}>{word}</p>)}

                    </div>
                    <select className="ml-2 rounded-md w-32" id="Word" onChange={(e) =>
                    {var selectBox = document.getElementById("Word");
                        const dayAway = selectBox.options[selectBox.selectedIndex].value;
                        setDateCalorie(getDateFromToday(dayAway))
                        setDaysCalorie(parseInt(dayAway));
                    }}>
                        <option value="7">Last 7 days</option>
                        <option value="30">Last 30 days</option>
                        <option value="365">Last 365 days</option>
                    </select>
                </div>
            </div>


            <div className="flex flex-col gap-2 inset-y-0 right-0 w-2/5 px-12 pt-2">
                <div className='flex flex-col border border-gray-400 pt-0 rounded-xl w-full shadow-lg'>
                    <a className="text-center justify-center font-bold">Emotional Health</a>
                <canvas id='emotionChart'></canvas>
                  <select className="ml-2 rounded-md w-32" id="Emotion" onChange={(e) =>
                  {var selectBox = document.getElementById("Emotion");
                      const dayAway = selectBox.options[selectBox.selectedIndex].value;
                      setDateEmotion(getDateFromToday(dayAway))
                      setDaysEmotion(parseInt(dayAway));
                  }}>
                      <option value="7">Last 7 days</option>
                      <option value="30">Last 30 days</option>
                      <option value="365">Last 365 days</option>
                  </select>
              </div>
                <div className='flex flex-col border border-gray-400 pt-0 mt-7 rounded-xl w-full shadow-lg'>
                    <a className="text-center justify-center font-bold">Heart Rate Monitor</a>
                <canvas id='heartChart'></canvas>
                  <select className="ml-2 rounded-md w-32" id="Heart" onChange={(e) =>
                  {var selectBox = document.getElementById("Heart");
                      const dayAway = selectBox.options[selectBox.selectedIndex].value;
                      setDateHeart(getDateFromToday(dayAway))
                      setDaysHeart(parseInt(dayAway));
                  }}>
                      <option value="7">Last 7 days</option>
                      <option value="30">Last 30 days</option>
                      <option value="365">Last 365 days</option>
                  </select>
              </div>

            </div>
        </div>
      </>
  )
}


function getDateFromToday(days) {
    const date = new Date();
    date.setDate(date.getDate() - days);
    return date.toISOString().split('T')[0]
}

export default Example;