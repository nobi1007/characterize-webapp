import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faCaretUp,
  faCaretDown,
  faCog,
  faSearch,
  faArrowsAltV,
  faBullseye,
  faBell,
  faEye,
  faFlagCheckered,
  faChartBar,
  faTable,
  faHeart,
  faPlus,
  faBookmark,
  faTags,
  faStickyNote,
  faColumns,
  faFilter,
  faTimes,
  faSignal,
  faBook,
  faEdit,
  faCheck,
  faTrash,
  faPlusCircle,
  faQuestion
} from "@fortawesome/free-solid-svg-icons";
import "./styles/scss/index.scss";
import * as Sentry from '@sentry/browser';
import "./polyfill.d";

Sentry.init({ 
  dsn: 'https://f1b819c7a5a34cd0b10b9211c593c2f4@sentry.io/1470444',
  integrations(integrations) {
    return integrations.filter(integration => integration.name !== 'Breadcrumbs');
  }
});

library.add(faCaretUp, faCaretDown, faCog, faSearch, faArrowsAltV, faBullseye, faPlusCircle, faBell, faEye, faFlagCheckered, faChartBar, faTable, faHeart, faPlus, faTags, faBookmark, faStickyNote, faColumns, faFilter, faTimes, faSignal, faBook, faEdit, faCheck, faTrash, faQuestion);

