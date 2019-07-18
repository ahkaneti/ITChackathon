import React from 'react';
// import ReactDOM from 'react-dom'
//imports for the map
import { compose, withProps } from "recompose";
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps";
//Imports from bootstrap 
import { Form, Button, ButtonGroup, Modal } from 'react-bootstrap';
import MapWithAMarker from './MapWithAMarker';
import FriendAdd from './FriendAdd';


//Imports for style
import './main.css';

let lat = 37.7749;
let lng = -122.4194;


class MainPage extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      // Sets that initial state
      lat: 0,
      lang: 0,
    };
  }
  showCurrentLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => {
          this.setState(prevState => ({
            currentLatLng: {
              ...prevState.currentLatLng,
              lat: position.coords.latitude,
              lng: position.coords.longitude
            },
            currentLatLng2: {
              ...prevState.currentLatLng2,
              lat: 32.109333, 
              lng: 34.855499,
            },
            isMarkerShown: true
          }))
        }
      )
    } else {
      console.log('error');
    }
  }
  componentDidMount() {
    this.showCurrentLocation()
  }
  searchLocation() {
    //search internet for address
    //get global lat and lang
    //take the map to the lat and lang
    //done
    return;
  }
  createRoute() {
    //Find a route between two addresses and display on map
  }
  render() {
    return (
      <div className='screen'>
        < link
          rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous"
        />
        <div className='bar'>
          <div className='navbar'>
            <Form className='nav-control'>
              <Form.Group>
                <Form.Label>Source</Form.Label>
                <Form.Control type="email" placeholder="Shoken 18" style={{ fontSize: 12, }} />
                <Form.Label>Destination</Form.Label>
                <Form.Control type="email" placeholder="Enter destination address" style={{ fontSize: 12, }} />
                <Form.Text className="text-muted">
                </Form.Text>
              </Form.Group>
            </Form>
            <FriendAdd className="search"/>
          </div >
        </div>
        <div className="map-container">
          <MapWithAMarker
            isMarkerShown={this.state.isMarkerShown}
            currentLocation={this.state.currentLatLng}
            currentLocation2={this.state.currentLatLng} />
        </div>
      </div>
    );
  }
}

export default MainPage;