import React from 'react';
import { compose, withProps } from "recompose";
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"
import logo from './logo.svg';
import './App.css';

const MyMapComponent = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `900px` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }),
  withScriptjs,
  withGoogleMap
)((props) =>
  <GoogleMap
    defaultZoom={8}
    defaultCenter={{ lat: 37.7749, lng: -122.4194 }}
  >
    {props.isMarkerShown && <Marker position={{ lat: 37.7749, lng: -122.4194 }} />}
  </GoogleMap>
)

function App() {
  return (
  < div> <MyMapComponent isMarkerShown /></div>
  );
}

export default App;
