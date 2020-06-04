import React, { Component} from 'react'
import db from '../FirestoreConfig';
import {Table, Button, Row, Col, InputGroup, Input} from 'reactstrap';

export default class Peliculas extends Component{

    state={
        pelis:[],
        inputValue:'',
        edit: false,
        id:''
    }

    componentDidMount(){
        db.collection('peliculas').onSnapshot((snapShots)=>{
            this.setState({
                pelis:snapShots.docs.map( doc=>{
                    // console.log(doc.data());
                    return{id:doc.id,data:doc.data()}
                })
            })
        })
    }

    changeValue = (e)=>{
        this.setState({
            inputValue:e.target.value
        })
    }

    action=()=>{
        const{inputValue, edit}=this.state;
        
        !edit ?
        db.collection("peliculas").add({
            title:inputValue
        }).then( ()=> {
            console.log('Agregado')
        }).catch(()=>{
            console.log('error')
        }) :
        this.update();
    }

    getPelicula=(id)=>{
        let docRef=db.collection("peliculas").doc(id);

        docRef.get().then((doc)=>{
            if(doc.exists){
                this.setState({
                    inputValue:doc.data().title,
                    edit:true,
                    id:doc.id
                })
            }else{
                console.log("El documento no existe")
            }
        }).catch((error)=>{
            console.log(error)
        })
    };

    update = () =>{
        const{id, inputValue}=this.state;
        db.collection("peliculas").doc(id).update({
            title:inputValue
        }).then(()=>{
            console.log('actualizado')
        }).catch((error)=>{
            console.log(error);
        })
    };

    deletePelicula=(id)=>{
        db.collection("peliculas").doc(id).delete();
    }

    render(){
        const {pelis, inputValue} = this.state;
        return(
            <div style={{textAlign: "center", paddingTop:"20px"}}>
                <h1>Gestión de películas</h1>
                <Row>
                    <Col xs="10">
                        <InputGroup>
                            <Input
                                placeholder="Agregar una nueva pelicula"
                                value={inputValue}
                                onChange={this.changeValue}
                            />
                        </InputGroup>
                    </Col>
                    <Col xs="2">
                        <div>
                            <Button onClick={this.action}>
                                {this.state.edit ? 'Editar':'Agregar'}
                            </Button>
                        </div>
                    </Col>
                </Row>
                <Table style={{textAlign: "center", paddingLeft:"350px",paddingTop:"30px"}}>
                    <thead>
                        <tr>
                            <th style={{width:"300px"}}>Pelicula</th>
                            <th style={{width:"100px"}}>Editar</th>
                            <th>Eliminar</th>
                        </tr>
                    </thead>
                    <tbody>
                        { pelis && pelis!==undefined?pelis.map((peli,key)=>(
                            <tr key={key}>
                                <td style={{width:"300px"}}>{peli.id}</td>
                                <td style={{width:"100px"}}><Button onClick={()=>this.getPelicula(peli.id)}>Editar</Button> </td>
                                <td style={{width:"100px"}}><Button onClick={()=>this.deletePelicula(peli.id)}>Eliminar</Button> </td>
                            </tr>
                        )):null}
                    </tbody>
                </Table>
            </div>
        )
    }
}