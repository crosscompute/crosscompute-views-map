window.{{ element_id }}_features = {
    type: "FeatureCollection",
    features: [
    ]
}
function App() {
    const [features, setFeatures] = $.React.useState(window.{{ element_id }}_features);
    const [mode, setMode] = $.React.useState(() => $.Nebula.Modes.DrawPolygonMode);
    const [selectedFeatureIndexes] = $.React.useState([]);

    const layer = new $.Nebula.Layers.EditableGeoJsonLayer({
        data: features,
        mode,
        selectedFeatureIndexes,
        onEdit: ({ updatedData }) => {
            window.{{ element_id }}_features = updatedData;
            console.log(updatedData)
            setFeatures(updatedData);
        }
    });

    return $.React.createElement("div", null,
        $.React.createElement($.Nebula.DeckGL, {
            initialViewState: {{map}},
            controller: {
                doubleClickZoom: false
            },
            layers: [layer],
            getCursor: layer.getCursor.bind(layer)

        },
            $.React.createElement($.StaticMap, {
                mapboxAccessToken: $.Nebula.accessToken,
                mapStyle: '{{ style_uri }}'
            })
        ),
        $.React.createElement("div", {
            style: { position: "absolute", top: 0, right: 0, color: "white" }
        },

            $.React.createElement("button", {
                onClick: () => setMode(() => $.Nebula.Modes.DrawPointMode),
                style: { background: mode === $.Nebula.Modes.DrawPointMode ? "#3090e0" : null }
            }, "Point"),
            $.React.createElement("button", {
                onClick: () => setMode(() => $.Nebula.Modes.DrawLineStringMode),
                style: { background: mode === $.Nebula.Modes.DrawLineStringMode ? "#3090e0" : null }
            }, "Line"),
            $.React.createElement("button", {
                onClick: () => setMode(() => $.Nebula.Modes.DrawPolygonMode),
                style: { background: mode === $.Nebula.Modes.DrawPolygonMode ? "#3090e0" : null }
            }, "Polygon")
        )
    )
}

var container = document.getElementById('{{ element_id }}');
var root = $.ReactDOM.createRoot(container);
root.render($.React.createElement(App, null));


MAP_BY_ELEMENT_ID['{{ element_id }}'] = {{ element_id }};
