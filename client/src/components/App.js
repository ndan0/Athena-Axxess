import styles from "@/styles/Chat.module.css";
import plane from "@/assets/paperline.png"
import React, { useState, useEffect, useRef } from "react";
import Head from "next/head";
import Image from 'next/image';
import SendIcon from '@/components/SendIcon'
import MicIcon from '@/components/Microphone'
import { useReactMediaRecorder } from "react-media-recorder";


export default function App() {

    const classes =
        [


        "My Health"

    ]
    const [selectedClass, setSelectedClass] = useState(0)
    const ref = useRef(null);

    const { status, startRecording, stopRecording, mediaBlobUrl, previewAudioStream, previewStream } =
    useReactMediaRecorder({ video: false, audio: true, mediaRecorderOptions: {
        mimeType: 'audio/webm'
    }, onStop: async (_, blob)=>{
        setLoading(true)
        console.log({blob})
        const body = new FormData();
        body.append("file", blob);
        const res = await fetch("http://localhost:8000/conversation/0/audio", {
            body, method: "POST"
        })
        const result = await res.json();
        console.log({result})
        setChat(result.messages)
        setLoading(false)
    } });

    useEffect(() => {console.log({status, mediaBlobUrl, previewAudioStream, previewStream})}, [status]);

  const [chat, setChat] = useState([])

useEffect(() => {
  ref.current && ref.current.scrollIntoView({alignToTop: true, behavior: "smooth"})
}, [chat])

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const handleSubmit = async (e) => {

    e.preventDefault();
    setChat((prev) => [...prev, {
        role: "user",
        content: message
    }])
    setMessage("")
    setLoading(true);


    const endpoint = "http://localhost:8000/conversation/0/text";

    const options = {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message
      }),
    };
    
    const response = await fetch(endpoint, options);

    const result = await response.json();

    setChat(result.messages)
    
    console.log(result);
    setLoading(false);

  };

useEffect(() => {
    if (chat.length > 0 && chat[chat.length - 1].role == "assistant") {
        const action = async () => {
            await fetch("http://localhost:8000/tts?text="+encodeURIComponent(chat[chat.length - 1].content))
        }
        action()
    }
}, [chat])

  return (
    <div className={styles.container}>
      <Head>
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"
        />
      </Head>

      
        <div className={styles.mainWrapper + " " + "overflow-scroll"}>
        <div className={styles.menu}>
          <button className={styles.newBtn}><span className="material-symbols-outlined">add</span> New Subject</button>
        {classes.map((course, index) => (
          <button className={index == selectedClass ? styles.active : ''} key={`course-${index}`} onClick={()=>setSelectedClass(index)}><span className="material-symbols-outlined }">chat</span> {course}</button>
          ))}
          <button className={styles.resetBtn} onClick={()=>{
            setChat([])
          }}><span className="material-symbols-outlined">device_reset</span> Reset Chat</button>
        </div>
      <div className={styles.ChatBox}>
      {
        chat.length == 0 ? 
      <div className={styles.titleContainer}>
      <span class="material-symbols-outlined">health_and_safety</span>
        <p className={styles.title}>Athena</p>
      </div> : ""
        }
        {chat.map((message, index) => {
            console.log(message)
            return(

          <div
            key={index}
            className={`${styles.message} ${
              message.role === "assistant"
                ? styles.assistant_msg
                : styles.user_msg
            }`}
          >
            <div className={styles.icon + " " + (message.role == "user" ? styles.userIcon : styles.aiIcon)}>
              {message.role == "user" ? (
                <span className="material-symbols-outlined">account_circle</span>
              ) : (
                <span className="material-symbols-outlined">neurology</span>
              )}
            </div>
            <p style={{whiteSpace: "pre-line"}}>{message.content}</p>
          </div>
        )})}
        
        {loading && <div
            className={`${styles.message} ${styles.assistant_msg
            }`}
          >
            <div className={styles.icon + " " + (styles.aiIcon)}>
              <span className="material-symbols-outlined">neurology</span>
              
            </div>
            <span className={"material-symbols-outlined loader"}>
            cached
</span>
          </div>}
          <span ref={ref}></span>
          <form onSubmit={(e)=>{
        e.preventDefault()
        handleSubmit(e)
      }}>
        <div className={styles.inputContainer}>
          <input
          className={styles.inputField}
            placeholder={"Ask a question about " + classes[selectedClass] + "..."}
            onChange={(e) => setMessage(e.target.value)}
            type="text"
            id="message"
            name="message"
            value={message}
            minLength="3"
          />
           <button
            onClick={handleSubmit}
            className={styles.enterButton}
          >
            <SendIcon height={25} width={25}></SendIcon>
          </button>
            <button

                type="button"
                onClick={()=> {
                    if (status === "recording") {
                        stopRecording();
                    } else {
                        startRecording();
                    }
                }}
                className={styles.micButton + " " + (status === "recording" ? "animate-pulse" : "")}
                style={{color: status === "recording" ? "#b9243c" : "black"}}
            >
                <MicIcon className="" style={{color: status === "recording" ? "#b9243c" : "black"}} height={25} width={25}></MicIcon>
            </button>
          </div>
        </form>
      <div className={styles.fade}></div>
      </div>
</div>
      
    </div>
  );
}
