function Heder() {
  return (
    <>
      <div className="navbar">
        <div className="content">
          <ul>
            <li>Dashboard</li>
            <li>Master Price</li>
            <li>Custom Price</li>
            <li>Calendar</li>
            <li>Reports</li>
          </ul>
        </div>

        <div className="icons">
          <div className="notification size"></div>
          <div className="avater size"></div>
        </div>
      </div>

      <div className="sub_header">
        <h3>Master Price</h3>
        <hr />
      </div>

      <div className="filter__button">
        <button>Round Trip</button>
        <button>One Way</button>
        <button>Multi City</button>
      </div>
    </>
  );
}

export default Heder;
