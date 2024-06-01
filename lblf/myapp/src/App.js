import React, { useState, useEffect } from 'react';
import HelloWorld from './HelloWorld';
import AuthForm from './AuthForm';

function App() {
  useEffect(() => {
    const metaGoogleSiteVerification = document.createElement('meta');
    metaGoogleSiteVerification.name = 'google-site-verification';
    metaGoogleSiteVerification.content = 'VIKuYg7UylPsJbHaui7Mi6KvVdd0FXFo2nZnfVtwtzU';
    document.head.appendChild(metaGoogleSiteVerification);
  }, []);

  return (
    <div class="container mx-auto middle-block">
      <div>
        <HelloWorld />
      </div>
      <div class="bg-white">
        <AuthForm/>
      </div>
    </div> 
  );
}

export default App;