import { useEffect } from "react"
import { Chart } from "chart.js";
function Example() {
    useEffect(() => {
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bubble',
            data: {
                datasets: [{
                    data: [
                        { x: 17, y: 3, r: 11 },
                    ],
                    label: "Team A",
                    borderColor: "rgb(75, 192, 192 )",
                    backgroundColor: "rgb(75, 192, 192,0.5)",
                    borderWidth: 2,

                }, {
                    data: [
                        { x: 10, y: 3, r: 20 },
                    ],
                    label: "Team B",
                    borderColor: "rgb(255, 205, 86)",
                    backgroundColor: "rgb(255, 205, 86, 0.5)",
                    borderWidth: 2,

                }, {
                    data: [
                        { x: 4, y: 14, r: 30 },
                    ],
                    label: "Team C",
                    borderColor: "rgb(255, 99, 132)",
                    backgroundColor: "rgb(255, 99, 132,0.5)",
                    borderWidth: 2,

                }
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: '# of wins'
                        }
                    }],
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: '# of games'
                        }
                    }],
                }
            },
        });
    }, [])


    return (
        <>
            {/* Bubble chart */}
            <h1 className="w-[150px] mx-auto mt-10 text-xl font-semibold capitalize ">Bubble Chart</h1>
            <div className="w-[1100px] h-screen flex mx-auto my-auto">
                <div className='border border-gray-400 pt-0 rounded-xl  w-full h-fit my-auto  shadow-xl'>
                    <canvas id='myChart'></canvas>
                </div>
            </div>
        </>
    )
}

export default Example;