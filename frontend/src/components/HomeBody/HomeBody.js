import React, { PureComponent } from "react";
import { Grid, Segment } from "semantic-ui-react";
import axios from "axios";
import "./HomeBody.scss";
import CustomUpload from "./CustomUpload";
import { SERVER_PATH } from "../../utilities/serverPath";

class HomeBody extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      isImageLoaded: false,
      loaded_image_uri: "",
      uploaded_file: undefined,
      characterized_image_uri: undefined,
      characterized_image_data: undefined,
    };
  }

  handleImageUpload = (e) => {
    const { uploaded_file } = this.state;
    e.preventDefault();

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
        });
        console.log(characterized_image_data);
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
    } = this.state;

    return (
      <div className="home-body">
        <Grid stackable columns={2}>
          <Grid.Column>
            <Segment>
              <CustomUpload
                handleFileOnChange={this.handleFileOnChange}
                handleImageUpload={this.handleImageUpload}
                isImageLoaded={isImageLoaded}
                loaded_image_uri={loaded_image_uri}
              />
            </Segment>
          </Grid.Column>
          <Grid.Column className="output-data-column">
            <Segment>
              {characterized_image_data && (
                <code className="output-data">{characterized_image_data}</code>
              )}
            </Segment>
          </Grid.Column>
        </Grid>
      </div>
    );
  }
}

export default HomeBody;
