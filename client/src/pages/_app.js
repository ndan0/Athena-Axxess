import '@/styles/globals.css'
import Navbar from '@/components/NavBar'
import {DevSupport} from "@react-buddy/ide-toolbox-next";
import {ComponentPreviews, useInitial} from "@/components/dev";

export default function App({Component, pageProps}) {
    return (
        <div className = "h-screen overflow-clip">
            <Navbar/>
            <DevSupport ComponentPreviews={ComponentPreviews}
                        useInitialHook={useInitial}
            >
                <Component {...pageProps} />
            </DevSupport>
        </div>
    )
}
