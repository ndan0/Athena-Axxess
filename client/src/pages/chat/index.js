import dynamic from "next/dynamic"

export default function Chat() {
  const App = dynamic(() => import('@/components/App'), { ssr: false });
  return <App />;
}

