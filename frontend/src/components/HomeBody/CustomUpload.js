/**
 * @author Shyam Mittal
 * @email mittalshyam1007@gmail.com
 * @create date 2020-08-13 21:42:48
 * @modify date 2020-08-13 21:42:48
 * @desc [description]
 */

import React, { PureComponent } from "react";
import { Input, Button, Icon } from "semantic-ui-react";
import "./HomeBody.scss";

class CustomUpload extends PureComponent {
  render() {
    const {
      isImageLoaded,
      loaded_image_uri,
      handleFileOnChange,
      handleImageUpload,
      isLoadingResponse,
      characterized_image_uri,
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
          size="large"
          style={{ color: "#24292e" }}
        />
        <div className="button-container">
          <Button
            className="characterize-it-button"
            onClick={handleImageUpload}
            content="Characterize it"
            disabled={!isImageLoaded}
            loading={isLoadingResponse}
          />
          <a
            href={characterized_image_uri}
            title="Download Characterized Image"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Button
              disabled={!characterized_image_uri}
              icon={<Icon name="download" />}
            />
          </a>
        </div>
      </div>
    );
  }
}

export default CustomUpload;
