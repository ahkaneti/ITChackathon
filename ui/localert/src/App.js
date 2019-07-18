import React from 'react';
// import ReactDOM from 'react-dom'
//imports for the map
import { compose, withProps } from "recompose";
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps";
//Imports from bootstrap 
import { Form } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import { ButtonGroup } from 'react-bootstrap';

//Imports for style
import './App.css';

let lat = 37.7749; 
let lng = -122.4194;



const MyMapComponent = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }),
  withScriptjs,
  withGoogleMap
)((props) =>
  <GoogleMap
    defaultZoom={18}
    defaultCenter={{ lat: lat, lng: lng }}
  >
    {/* {props.isMarkerShown && <Marker position={{ lat: lat, lng: lng}} />} */}
    <ButtonGroup style={{position: 'absolute', bottom:70, left: 900,}}>
      <Button style={{backgroundColor: 'red'}}>Alert</Button>
      <Button syle ={{backgroundColor: 'black'}}>Report</Button>
    </ButtonGroup>
  </GoogleMap>
)

class App extends React.Component{
  constructor(props) {
    super(props);

    this.state = {
      // Sets that initial state
      height: 0,
    };
  }
  render(){
  return (
    <div className='screen'>
      < link
        rel = "stylesheet"
        href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity = "sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        crossorigin = "anonymous"
      />  
      <div className= 'bar'>
        <div className = 'navbar'>
          <Form className='nav-control'>
            <Form.Group>
              <Form.Label>Source</Form.Label>
              <Form.Control type="email" placeholder="Enter source address" style={{fontSize:  12,}}/>
              <Form.Label>Destination</Form.Label>
              <Form.Control type="email" placeholder="Enter destination address" style={{ fontSize: 12, }} />
              <Form.Text className="text-muted">
                We'll never share your email with anyone else.
              </Form.Text>
            </Form.Group>
          </Form>
          <Button style={{ fontSize: 12, marginLeft:35}}>Search Route</Button>
        </div >
      </div>
      <div  className="map-container"> 
        <MyMapComponent isMarkerShown />
      </div>
    </div>
  );
}
}

export default App;