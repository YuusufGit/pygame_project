This doesn't require any images, the character and objects are made with surfaces.
Simply get the SSH link of this project or fork this project then do that and then link it with your local machine.
Then load it into visual studio code so you can see the code and run it.

Here's a mermaid flowchart of how it works:

flowchart TD
    A[Start] --> B[Initialize Pygame]
    B --> C[Set screen size and background color]
    C --> D[Create fonts and surfaces for player and bombs]
    D --> E[Main game loop]
    E --> F[Handle events]
    F --> G[Check for quit event]
    F --> H[Handle key presses]
    H --> I{W key pressed?}
    I -->|Yes| J[Move player up]
    I -->|No| K{S key pressed?}
    K -->|Yes| L[Move player down]
    K -->|No| M{A key pressed?}
    M -->|Yes| N[Move player left]
    M -->|No| O{D key pressed?}
    O -->|Yes| P[Move player right]
    F --> Q[Handle key releases]
    Q --> R{W key released?}
    R -->|Yes| S[Stop moving player up]
    R -->|No| T{S key released?}
    T -->|Yes| U[Stop moving player down]
    T -->|No| V{A key released?}
    V -->|Yes| W[Stop moving player left]
    V -->|No| X{D key released?}
    X -->|Yes| Y[Stop moving player right]
    F --> Z[Spawn bombs event]
    Z --> AA[Create bomb at random position]
    AA --> AB[Set bomb speed]
    E --> AC[Move bombs down]
    AC --> AD[Remove off-screen bombs]
    E --> AE[Check player collision with bombs]
    AE --> AF{Collision detected?}
    AF -->|Yes| AG[Reset game and score]
    AF -->|No| AH[Continue game]
    E --> AI[Update display]
    AI --> AJ[Repeat loop]

    classDef default fill:#f9f,stroke:#333,stroke-width:4px;
    class A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,AH,AI,AJ default;
