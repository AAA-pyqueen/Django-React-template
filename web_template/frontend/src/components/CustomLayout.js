import React from 'react';
import './custom_styles.css';

function CustomLayout({ children }) {
    return (
        <div className="custom-layout">
            <header>
                <h1>Custom Layout</h1>
            </header>
            <main>
                {children}
            </main>
        </div>
    );
}

export default CustomLayout;