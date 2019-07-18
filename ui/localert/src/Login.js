import React from 'react';
import './login.css'
import {Accordion, Card, Button, Form} from 'react-bootstrap';


class Login extends React.Component{
  constructor(props)
  {
    super(props);
    this.state = {
      username: '',
      password: '',
    }
  }
  render(){
    return (
      <div className='screen'>
        <link
          rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous"
        />
        <div className = 'screenADJ'>
          <Accordion>
            <Card>
              <Card.Header>
                <Accordion.Toggle as={ Button } variant="link" eventKey="0">
                Login
                </Accordion.Toggle>
              </Card.Header>
              <Accordion.Collapse eventKey="0">
                <Card.Body>
                  <Form.Group>
                    <Form.Label>First Name and Last Name</Form.Label>
                    <Form.Control type="email" placeholder="Username" style={{ fontSize: 12, }} />
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" style={{ fontSize: 12, }} />
                    <Form.Text className="text-muted">
                      <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Forgot Password?</a>
                    </Form.Text>
                  </Form.Group>
                  <Button><a className = "linkMap"href="http://localhost:3000/map" >Login!</a></Button>
                  </Card.Body>
              </Accordion.Collapse>
            </Card>
            <Card>
              <Card.Header>
                <Accordion.Toggle as={Button} variant="link" eventKey="1">
                  Create a User
                </Accordion.Toggle>
              </Card.Header>
              <Accordion.Collapse eventKey="1">
                <Card.Body>
                  <Form.Group>
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="email" placeholder="Username" style={{ fontSize: 12, }} />
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="email" placeholder="Password" style={{ fontSize: 12, }} />
                    <Form.Label>Repeat Password</Form.Label>
                    <Form.Control type="email" placeholder="Password" style={{ fontSize: 12, }} />
                  </Form.Group>
                  <Button>Create User!</Button>
                </Card.Body>
              </Accordion.Collapse>
            </Card>
          </Accordion>
        </div>
      </div>
    );
  }
}

export default Login;