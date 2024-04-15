import { createContext,useContext,useState,useEffect } from "react";
const ThemeContext = createContext();

// document.querySelector('.intro').style.backgroundImage = "url('../img/intro2-bg.jpg')";
export const useTheme = ()=>{
    return useContext(ThemeContext);
};

export const ThemeProvider = ({children})=>{
    const [isDarkMode,setIsDarkMode] = useState(false);

    const toggleTheme = ()=>{
        setIsDarkMode((prevState)=>!prevState);
    };

    const theme = isDarkMode ? "dark":"light";

    useEffect(()=>{
        document.documentElement.setAttribute("data-theme",theme);
        /* if(theme==="dark")
          document.querySelector('.intro').style.background = "url('../img/intro-bg9.jpg') ";
         else
         document.querySelector('.intro').style.background = "url('../img/intro-bg.jpg')";*/
    },[isDarkMode,theme])
    

    return <ThemeContext.Provider value={{theme,toggleTheme}}>{children}</ThemeContext.Provider>
}