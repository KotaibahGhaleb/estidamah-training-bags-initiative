import { useState } from 'react'
import './App.css'

function App() {
  const [isPlaying, setIsPlaying] = useState(false)

  return (
    <div className="w-full h-screen bg-[#f3f5ee] flex items-center justify-center overflow-hidden">
      {isPlaying ? (
        <video
          className="w-full h-full object-contain bg-black"
          autoPlay
          onEnded={() => setIsPlaying(false)}
        >
          <source src="/فيديو مبادرة الحقائب التدريبية - 40 ثانية.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      ) : (
        <div className="relative">
          <img
            src="/الشاشة الختامية - مبادرة الحقائب التدريبية.png"
            alt="Training Bags Initiative"
            className="block max-w-screen max-h-screen w-auto h-auto"
          />
          <button
            onClick={() => setIsPlaying(true)}
            className="absolute left-1/2 -translate-x-1/2 -translate-y-1/2 w-[7%] aspect-square min-w-[40px] min-h-[40px] bg-yellow-400 rounded-full flex items-center justify-center hover:bg-yellow-500 transition-colors cursor-pointer shadow-lg"
            style={{ top: '57%' }}
          >
            <svg
              className="w-1/2 h-1/2 text-white ml-[8%]"
              fill="currentColor"
              viewBox="0 0 24 24"
            >
              <path d="M8 5v14l11-7z" />
            </svg>
          </button>
        </div>
      )}
    </div>
  )
}

export default App
