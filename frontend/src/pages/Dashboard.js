import { useEffect, useState } from "react";
import api from "../api";
import { TextField, Card, CardContent, Typography, Badge } from "@mui/material";

export default function Dashboard() {
  const [events, setEvents] = useState([]);
  const [filter, setFilter] = useState("");
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    api.get("events/")
      .then(res => {
        setEvents(res.data);
        // Notification example: show events created today
        const today = new Date().toISOString().split("T")[0];
        const newEvents = res.data.filter(e => e.date === today);
        setNotifications(newEvents);
      })
      .catch(err => console.error("Failed to load events", err));
  }, []);

  const filteredEvents = events.filter(e => e.name.toLowerCase().includes(filter.toLowerCase()));

  return (
    <div style={{ padding: "20px" }}>
      <Typography variant="h4">Dashboard</Typography>

      <Badge badgeContent={notifications.length} color="secondary">
        <Typography>Notifications</Typography>
      </Badge>

      <TextField
        label="Search Events"
        variant="outlined"
        size="small"
        value={filter}
        onChange={e => setFilter(e.target.value)}
        style={{ margin: "20px 0", width: "100%" }}
      />

      {filteredEvents.map(e => (
        <Card key={e.id} style={{ marginBottom: "15px" }}>
          <CardContent>
            <Typography variant="h6">{e.name}</Typography>
            <Typography>Location: {e.location}</Typography>
            <Typography>Date: {e.date}</Typography>
            <Typography>Tasks:</Typography>
            {e.tasks.map(t => (
              <Typography key={t.id} style={{ marginLeft: "20px" }}>
                - {t.title} ({t.assigned_to?.username || "Unassigned"}) [{t.completed ? "Done" : "Pending"}]
              </Typography>
            ))}
          </CardContent>
        </Card>
      ))}

      {filteredEvents.length === 0 && <Typography>No events found</Typography>}
    </div>
  );
}
