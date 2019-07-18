import React from 'react';
import { compose, withProps } from "recompose";
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps";
import { Button, ButtonGroup, Modal, ButtonToolbar } from 'react-bootstrap';
import ModalV from './FriendAlert'


const MapWithAMarker = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }),
  withScriptjs,
  withGoogleMap
)((props) =>
  <GoogleMap
    defaultZoom={13}
    center={{ lat: props.currentLocation.lat, lng: props.currentLocation.lng }}
  >
    {props.isMarkerShown && <Marker position={{ lat: props.currentLocation.lat, lng: props.currentLocation.lng }} onClick={props.onMarkerClick} />}
    {/* <Marker position={{ lat: 32.08635, lng: 34.77479 }} onClick={props.onMarkerClick} style={{ display: 'none' }} /> */}
    {/* <Marker position={{ lat: 32.08913, lng: 34.77647 }} onClick={props.onMarkerClick} /> */}
    <ButtonGroup style={{ position: 'absolute', bottom: '5%', right: '35%' }}>
      <ButtonToolbar>
        
        <ModalV/>
        </ButtonToolbar>
      <Button>Report</Button>
    </ButtonGroup>
  </GoogleMap>
)

export default MapWithAMarker;