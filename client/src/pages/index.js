//Write a base login page with 2 user: user and nurse
import React, { useState, useEffect, useRef } from "react";
import styles from '../styles/Home.module.css'
import { useRouter } from "next/router";
import Head from "next/head";
import Image from 'next/image';

export default function Login() {


    return (
        <>
            <video autoPlay muted loop className={styles.video}>
                <source src=" https://axxessvideos.s3.amazonaws.com/axxessherovids/staffing.mp4" type="video/mp4"/>
            </video>
            <div className="flex flex-col items-start justify-center min-h-screen py-2 -mt-28 px-14 text-center">
                <div className="block max-w-md p-6 rounded-xl bg-gray-200 bg-opacity-60">
                    <h1 className="text-4xl mb-6 font-bold text-black">Introducing Athena</h1>
                    <h3 className="text-2xl font-bold text-black">A powerful, user-friendly virtual assistant for heath care at home</h3>
                    <a href="/login"
                       className="mt-8 inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-axx-red focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-axx-red  dark:focus:bg-axx-red">
                        Explore
                        <svg aria-hidden="true" className="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20"
                             xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                  clip-rule="evenodd"></path>
                        </svg>
                    </a>
                </div>

            </div>
        </>

    )

}
