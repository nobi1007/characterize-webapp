/**
 * @author Shyam Mittal
 * @email mittalshyam1007@gmail.com
 * @create date 2020-08-13 21:42:48
 * @modify date 2020-08-13 21:42:48
 * @desc [description]
 */

import React, { PureComponent } from "react";
import { Input, Button } from "semantic-ui-react";
import "./HomeBody.scss";

class CustomUpload extends PureComponent {
  render() {
    const {
      isImageLoaded,
      loaded_image_uri,
      handleFileOnChange,
      handleImageUpload,
      isLoadingResponse,
    } = this.props;
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
        <Input
          type="file"
          className="file-upload-input"
          onChange={handleFileOnChange}
          label="Choose an Image"
          size="large"
          style={{ color: "#24292e" }}
        />
        <Button
          onClick={handleImageUpload}
          content="Characterize it"
          disabled={!isImageLoaded}
          loading={isLoadingResponse}
        />
      </div>
    );
  }
}

export default CustomUpload;
