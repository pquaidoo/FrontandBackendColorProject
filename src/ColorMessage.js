import React, {useState, useEffect} from 'react';
import axios from 'axios';

const ColorMessage = () => {
    const [message, setMessage] = useState('');
    const [colorHistory, setColorHistory] = useState([]);


    useEffect(() => {
        
        fetchColorHistory();
      }, []);

    const fetchMessage = async(color) => {
        try{
            const response = await axios.get("http://127.0.0.1:8000/color/"+color);
            setMessage(response.data.message);
        }catch(error){
            setMessage('Error fetching color message.');

        }
    };
    const fetchColorHistory = async() => {
        try{
            const response = await axios.get("http://127.0.0.1:8000/colorHistory");
            setColorHistory(response.data);
        }catch(error){
            console.error('Error fetching color message.',error);

        }
    };
    const handleClearHistory = async () => {
        try {
          await axios.delete("http://127.0.0.1:8000/colorHistory");
          window.location.reload();
        } catch (error) {
          console.error('Error clearing history:', error);
        }
      };
    

    

    return (
        <div>
            
            <input type="text" id="color"/>
            <input type="button" value="Click" onClick = {() => fetchMessage((document.getElementById("color")).value)}/>
            
            <p>{message}</p>
            <input type="button" value="update" onClick = {() => fetchColorHistory()}/>
            <p>{colorHistory}</p>
            <input type="button" value="clear" onClick = {() => handleClearHistory()}/>
        </div>
    );
};

export default ColorMessage;

