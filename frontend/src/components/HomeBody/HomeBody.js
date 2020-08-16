import React, { PureComponent } from "react";
import { Grid, Segment, Icon } from "semantic-ui-react";
import axios from "axios";
import "./HomeBody.scss";
import CustomUpload from "./CustomUpload";
import { SERVER_PATH } from "../../utilities/serverPath";
import initImage from "../../images/characterize_github.jpg";
import { initImageData, initImageUri } from "./initImageData";

class HomeBody extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      isImageLoaded: true,
      loaded_image_uri: initImageUri,
      uploaded_file: initImage,
      characterized_image_uri: undefined,
      characterized_image_data: initImageData,
      isLoadingResponse: false,
    };
  }

  handleImageUpload = (e) => {
    const { uploaded_file } = this.state;
    e.preventDefault();
    this.setState({
      isLoadingResponse: true,
    });

    const formData = new FormData();
    formData.append("input_image", uploaded_file);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    const url = SERVER_PATH + `/show_image`;

    axios
      .create({
        withCredentials: true,
      })
      .post(url, formData, config)
      .then((response) => {
        const data = response.data;
        const characterized_image_uri = data["characterized-image-uri"];
        const characterized_image_data = data["characterized-image-data"];
        this.setState({
          characterized_image_data,
          characterized_image_uri,
          isLoadingResponse: false,
        });
        console.log("imageData", data);
      })
      .catch((error) => {
        this.setState({
          isLoadingResponse: false,
        });
      });
  };

  handleFileOnChange = (e) => {
    const file = e.target.files[0];
    const fileReader = new FileReader();

    fileReader.onload = () => {
      this.setState({
        uploaded_file: file,
        loaded_image_uri: fileReader.result,
        isImageLoaded: true,
      });
    };

    if (file) fileReader.readAsDataURL(file);
  };

  render() {
    const {
      isImageLoaded,
      loaded_image_uri,
      characterized_image_data,
      isLoadingResponse,
    } = this.state;

    return (
      <div className="home-body">
        <Grid stackable columns={2}>
          <Grid.Column>
            <Segment style={{ backgroundColor: "#24292e" }}>
              <CustomUpload
                handleFileOnChange={this.handleFileOnChange}
                handleImageUpload={this.handleImageUpload}
                isImageLoaded={isImageLoaded}
                loaded_image_uri={loaded_image_uri}
                isLoadingResponse={isLoadingResponse}
              />
            </Segment>
          </Grid.Column>
          <Grid.Column className="output-data-column">
            <Segment style={{ backgroundColor: "#24292e" }}>
              {characterized_image_data && (
                <>
                  <code className="output-data">
                    {characterized_image_data}
                  </code>
                </>
              )}
            </Segment>
          </Grid.Column>
        </Grid>
      </div>
    );
  }
}

export default HomeBody;
