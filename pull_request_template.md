<!-- Load `editable-table` directly from Pika's CDN -->
<script type="module" src="https://cdn.pika.dev/editable-table"></script>

<!-- put a normal <table> tag inside <editable-table> tags.
     The last <tr> in <tbody> becomes the template for new rows -->
<editable-table>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>E-Mail</th>
        <th colspan="99">Birthday</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <input name="name" placeholder="Joe Doe" autocomplete="off" />
        </td>
        <td>
          <input
            name="email"
            placeholder="joe@example.com"
            type="email"
            autocomplete="off"
          />
        </td>
        <td>
          <input
            name="birthday"
            placeholder="10/20/2000"
            type="date"
            required="required"
            autocomplete="off"
          />
        </td>
        <td>
          <span data-remove>×</span>
        </td>
      </tr>
    </tbody>
  </table>
</editable-table>