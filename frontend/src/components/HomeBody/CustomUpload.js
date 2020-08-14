/**
 * @author Shyam Mittal
 * @email mittalshyam1007@gmail.com
 * @create date 2020-08-13 21:42:48
 * @modify date 2020-08-13 21:42:48
 * @desc [description]
 */

import React, { PureComponent } from "react";
import { Input } from "semantic-ui-react";
import "./HomeBody.scss";

class CustomUpload extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      isImageLoaded: false,
      loaded_image_uri: "",
    };
  }

  handleFileOnChange = (e) => {
    const file = e.target.files[0];
    const fileReader = new FileReader();

    fileReader.onload = () => {
      this.setState({
        loaded_image_uri: fileReader.result,
        isImageLoaded: true,
      });
    };

    fileReader.readAsDataURL(file);
  };

  render() {
    const { loaded_image_uri, isImageLoaded } = this.state;
    return (
      <div className="custom-upload">
        <div className="image-upload-container">
          {isImageLoaded && (
            <img
              className="image-upload"
              src={loaded_image_uri}
              alt="File to be uploaded"
            />
          )}
        </div>
        <Input type="file" onChange={this.handleFileOnChange} />
      </div>
    );
  }
}

export default CustomUpload;
