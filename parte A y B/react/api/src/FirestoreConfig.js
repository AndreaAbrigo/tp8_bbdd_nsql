import firebase from 'firebase';
import 'firebase/firestore';

firebase.initializeApp({
    apiKey: "AIzaSyB2CGP0vrlcLIAl9WXFoCrgfMR7pvI49MM",
    authDomain: "practica9-f6d35.firebaseapp.com",
    databaseURL: "https://practica9-f6d35.firebaseio.com",
    projectId: "practica9-f6d35",
    storageBucket: "practica9-f6d35.appspot.com",
    messagingSenderId: "643739959462",
    appId: "1:643739959462:web:bbbf8c244545aa2e0a7467",
    measurementId: "G-GXBMYW533K"
});
let db = firebase.firestore();
db.settings({timestampsInSnapshots:true});

export default db;