import React from "react";
import { useTheme } from "../theme-context";
export const Navigation = (props) => {

  const {theme,toggleTheme} = useTheme();
  return (
    <nav id="menu" className="navbar navbar-default navbar-fixed-top " >
      <div className="container">
        <div className="navbar-header">
          <button
            type="button"
            className="navbar-toggle collapsed "
            data-toggle="collapse"
            data-target="#bs-example-navbar-collapse-1"
          >
            {" "}
            <span className="sr-only">Toggle navigation</span>{" "}
            <span className="icon-bar"></span>{" "}
            <span className="icon-bar"></span>{" "}
            <span className="icon-bar"></span>{" "}
          </button>
          <a className="navbar-brand page-scroll" href="#page-top">
            MoodSync
          </a>{" "}
        </div>

        <div
          className="collapse navbar-collapse "
          id="bs-example-navbar-collapse-1"
        >
          <ul className="nav navbar-nav navbar-right">
            <li>
              <a href="#features" className="page-scroll">
                Features
              </a>
            </li>
            <li>
              <a href="#about" className="page-scroll">
                About
              </a>
            </li>
            {/* <li>
              <a href="#services" className="page-scroll">
                Services
              </a>
            </li> */}
            <li>
              <a href="#portfolio" className="page-scroll">
                Gallery
              </a>
            </li>
            {/* <li>
              <a href="#testimonials" className="page-scroll">
                Testimonials
              </a>
            </li> */}
            <li>
              <a href="#team" className="page-scroll">
                Team
              </a>
            </li>
            {/* <li>
              <a href="#contact" className="page-scroll">
                Contact
              </a>
            </li> */}
            <li>
              <div className="mode-switch">
                <label>
                  <input type="checkbox" onChange={toggleTheme}  checked={theme==='dark'}/>
                  <span className="slider round"></span>
                </label>
              </div>
            </li>
            
          </ul>
        </div>
      </div>
    </nav>
  );
};
