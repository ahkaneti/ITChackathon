import React from 'react';
import { Modal, Button, ButtonToolbar } from 'react-bootstrap';
import Multiselect from 'multiselect-dropdown-react';

const data = [{
  name: 'Elroi',
},
{
  name: 'Igor',
},
{
  name: 'Julia',
},
{
  name: 'Rotem',
},
{
  name: 'Aaron',
}];

function FriendAdd(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">Pick which friends you want to add to your navigation group.</Modal.Title>
      </Modal.Header>
      <Modal.Body
        className="modalv">
        <Multiselect options={data} onSelectOptions={{}}/>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

function Modals() {
  const [modalShow, setModalShow] = React.useState(false);
  // return (<Button style={{ backgroundColor: 'red' }}>Alert</Button>
  return (
    <ButtonToolbar style={{marginLeft: 15,}}>
      <Button variant="primary" onClick={() => setModalShow(true)}>
        Start Navigation
      </Button>

      <FriendAdd
        show={modalShow}
        onHide={() => setModalShow(false)}
      />
    </ButtonToolbar>
  );
}
export default Modals;