//Create a Nav bar component with Logo and 3 links
import React from "react";
import Link from "next/link";
import Image from "next/image";
import { useRouter } from "next/router";
import logo from "../assets/AxxessLogo.png";

const NavBar = () => {


}
export default function Navbar() {
    return (

        <div className="flex flex-row justify-between items-center bg-white p-4">
            <div className="flex flex-row items-center">
                <Image src={logo} height={50} />

            </div>
            <div className="flex flex-row items-center">
                <div href="/" ><a className="text-xl font-bold text-axx-red">Home</a></div>
                <div href="/login"><a className="text-xl font-bold">Login</a></div>
                <div href="/register"><a className="text-xl font-bold">Register</a></div>
            </div>
        </div>

    )
}