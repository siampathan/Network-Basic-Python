import { useState, useEffect } from "react";

import axios from "axios";
import DATA from "./data/LHR_CDG_ADT1_TYPE_1.txt";
import "./App.css";

function App() {
  const [jsonData, setJsonData] = useState(null);

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    try {
      const response = await axios.get(DATA);
      setJsonData(response.data.flightOffer);
      console.log(response.data.flightOffer);
    } catch (err) {
      console.error(err.message);
    }
  };

  return (
    <>
      <h3>Data Parsed successfully</h3>

      <div className="table__wrap">
        <table>
          <thead>
            <tr>
              <th>FLIGHT</th>
              <th>AIRCRAFT</th>
              <th>CLASS</th>
              <th>FARE</th>
              <th>ROUTE</th>
              <th>DEPARTURE</th>
              <th>ARRIVAL</th>
              <th>DURATION</th>
              <th>PRICE</th>
            </tr>
          </thead>

          <tbody>
            {jsonData?.map((data, indx) => (
              <tr key={indx}>
                <td>Alfreds Futterkiste</td>
                <td>Maria Anders</td>
                <td>
                  {data.class.map((classItem, index) => (
                    <div key={index}>
                      {classItem.map((item, subIndex) => (
                        <span key={subIndex}>
                          {item} <br />
                        </span>
                      ))}
                    </div>
                  ))}
                </td>

                <td>
                  {data.fareBasis.map((classItem, index) => (
                    <div key={index}>
                      {classItem.map((item, subIndex) => (
                        <span key={subIndex}>
                          {item} <br />
                        </span>
                      ))}
                    </div>
                  ))}
                </td>
                <td>
                  {data.itineraries.map((itinerary, index) => (
                    <div key={index}>{itinerary.duration}</div>
                  ))}
                </td>

                <td>{data.price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default App;
