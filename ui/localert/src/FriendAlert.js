import React from 'react';
import {Modal, Button, ButtonToolbar} from 'react-bootstrap';

function FriendAlert(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">Friend Alert!!!</Modal.Title>
      </Modal.Header>
      <Modal.Body
        className="modalv">
        <h4>ALERT!!!</h4>
        <p>
          Your friend has been stagnant for too long!!!!
        </p>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

function ModalV() {
  const [modalShow, setModalShow] = React.useState(false);
  // return (<Button style={{ backgroundColor: 'red' }}>Alert</Button>
  return (
    <ButtonToolbar>
      <Button variant="primary" onClick={() => setModalShow(true)} style={{ backgroundColor: 'red' }}>
        Alert
      </Button>

      <FriendAlert
        show={modalShow}
        onHide={() => setModalShow(false)}
      />
    </ButtonToolbar>
  );
}
export default ModalV;