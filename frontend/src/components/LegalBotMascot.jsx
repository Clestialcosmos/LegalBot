function LegalBotMascot() {
    return (
      <div className="relative flex items-center justify-center">
  
        {/* Background Glow */}
  
        <div className="absolute h-72 w-72 rounded-full bg-violet-300/30 blur-3xl animate-pulse"></div>
  
        {/* Floating Animation */}
  
        <div className="float-animation hover:scale-105 transition duration-500">
  
          <svg
            className="relative z-10 h-80 w-80 drop-shadow-2xl"
            viewBox="0 0 420 420"
            fill="none"
          >
  
            {/* Shadow */}
  
            <ellipse
              cx="210"
              cy="372"
              rx="92"
              ry="18"
              fill="#DDD6FE"
            />
  
            {/* Body */}
  
            <rect
              x="110"
              y="145"
              width="200"
              height="165"
              rx="42"
              fill="url(#body)"
            />
  
            {/* Head */}
  
            <rect
              x="95"
              y="40"
              width="230"
              height="140"
              rx="48"
              fill="url(#head)"
            />
  
            {/* Left Eye */}
  
            <circle
              cx="165"
              cy="105"
              r="15"
              fill="white"
            />
  
            <circle
              cx="165"
              cy="105"
              r="7"
              fill="#6D28D9"
            />
  
            {/* Right Eye */}
  
            <circle
              cx="255"
              cy="105"
              r="15"
              fill="white"
            />
  
            <circle
              cx="255"
              cy="105"
              r="7"
              fill="#6D28D9"
            />
  
            {/* Smile */}
  
            <path
              d="M170 145 Q210 175 250 145"
              stroke="white"
              strokeWidth="8"
              strokeLinecap="round"
            />
  
            {/* Antenna */}
  
            <line
              x1="210"
              y1="40"
              x2="210"
              y2="12"
              stroke="#7C3AED"
              strokeWidth="6"
            />
  
            <circle
              cx="210"
              cy="10"
              r="10"
              fill="#A855F7"
            >
  
              <animate
                attributeName="r"
                values="10;13;10"
                dur="2s"
                repeatCount="indefinite"
              />
  
            </circle>
  
            {/* Left Arm */}
  
            <line
              x1="110"
              y1="205"
              x2="55"
              y2="250"
              stroke="#7C3AED"
              strokeWidth="10"
              strokeLinecap="round"
            />
  
            {/* Right Arm */}
  
            <line
              x1="310"
              y1="205"
              x2="365"
              y2="250"
              stroke="#7C3AED"
              strokeWidth="10"
              strokeLinecap="round"
            />
  
            {/* Left Leg */}
  
            <line
              x1="170"
              y1="310"
              x2="150"
              y2="350"
              stroke="#7C3AED"
              strokeWidth="10"
              strokeLinecap="round"
            />
  
            {/* Right Leg */}
  
            <line
              x1="250"
              y1="310"
              x2="270"
              y2="350"
              stroke="#7C3AED"
              strokeWidth="10"
              strokeLinecap="round"
            />
  
            {/* Legal Icon */}
  
            <text
              x="210"
              y="255"
              fontSize="54"
              textAnchor="middle"
            >
              ⚖️
            </text>
  
            <defs>
  
              <linearGradient
                id="head"
                x1="0"
                y1="0"
                x2="1"
                y2="1"
              >
  
                <stop
                  offset="0%"
                  stopColor="#7C3AED"
                />
  
                <stop
                  offset="100%"
                  stopColor="#A855F7"
                />
  
              </linearGradient>
  
              <linearGradient
                id="body"
                x1="0"
                y1="0"
                x2="1"
                y2="1"
              >
  
                <stop
                  offset="0%"
                  stopColor="#8B5CF6"
                />
  
                <stop
                  offset="100%"
                  stopColor="#C084FC"
                />
  
              </linearGradient>
  
            </defs>
  
          </svg>
  
        </div>
  
      </div>
    );
  }
  
  export default LegalBotMascot;